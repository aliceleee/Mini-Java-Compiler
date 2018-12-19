// Generated from miniJavaExpr.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link miniJavaExprParser}.
 */
public interface miniJavaExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link miniJavaExprParser#goal}.
	 * @param ctx the parse tree
	 */
	void enterGoal(miniJavaExprParser.GoalContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniJavaExprParser#goal}.
	 * @param ctx the parse tree
	 */
	void exitGoal(miniJavaExprParser.GoalContext ctx);
	/**
	 * Enter a parse tree produced by {@link miniJavaExprParser#mainclass}.
	 * @param ctx the parse tree
	 */
	void enterMainclass(miniJavaExprParser.MainclassContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniJavaExprParser#mainclass}.
	 * @param ctx the parse tree
	 */
	void exitMainclass(miniJavaExprParser.MainclassContext ctx);
	/**
	 * Enter a parse tree produced by {@link miniJavaExprParser#classdeclaration}.
	 * @param ctx the parse tree
	 */
	void enterClassdeclaration(miniJavaExprParser.ClassdeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniJavaExprParser#classdeclaration}.
	 * @param ctx the parse tree
	 */
	void exitClassdeclaration(miniJavaExprParser.ClassdeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link miniJavaExprParser#vardeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVardeclaration(miniJavaExprParser.VardeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniJavaExprParser#vardeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVardeclaration(miniJavaExprParser.VardeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link miniJavaExprParser#methoddeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethoddeclaration(miniJavaExprParser.MethoddeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link miniJavaExprParser#methoddeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethoddeclaration(miniJavaExprParser.MethoddeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arraymjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void enterArraymjtype(miniJavaExprParser.ArraymjtypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arraymjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void exitArraymjtype(miniJavaExprParser.ArraymjtypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code booleanmjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void enterBooleanmjtype(miniJavaExprParser.BooleanmjtypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code booleanmjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void exitBooleanmjtype(miniJavaExprParser.BooleanmjtypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intmjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void enterIntmjtype(miniJavaExprParser.IntmjtypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intmjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void exitIntmjtype(miniJavaExprParser.IntmjtypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identifiermjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void enterIdentifiermjtype(miniJavaExprParser.IdentifiermjtypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identifiermjtype}
	 * labeled alternative in {@link miniJavaExprParser#mjtype}.
	 * @param ctx the parse tree
	 */
	void exitIdentifiermjtype(miniJavaExprParser.IdentifiermjtypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blockStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(miniJavaExprParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blockStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(miniJavaExprParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(miniJavaExprParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(miniJavaExprParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(miniJavaExprParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(miniJavaExprParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatement(miniJavaExprParser.PrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatement(miniJavaExprParser.PrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStatement(miniJavaExprParser.AssignStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignStatement}
	 * labeled alternative in {@link miniJavaExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStatement(miniJavaExprParser.AssignStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constIntExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterConstIntExpr(miniJavaExprParser.ConstIntExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constIntExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitConstIntExpr(miniJavaExprParser.ConstIntExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code createClassExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterCreateClassExpr(miniJavaExprParser.CreateClassExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code createClassExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitCreateClassExpr(miniJavaExprParser.CreateClassExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arraylenExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArraylenExpr(miniJavaExprParser.ArraylenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arraylenExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArraylenExpr(miniJavaExprParser.ArraylenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code thisExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterThisExpr(miniJavaExprParser.ThisExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code thisExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitThisExpr(miniJavaExprParser.ThisExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code createArrayExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterCreateArrayExpr(miniJavaExprParser.CreateArrayExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code createArrayExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitCreateArrayExpr(miniJavaExprParser.CreateArrayExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrayValExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterArrayValExpr(miniJavaExprParser.ArrayValExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrayValExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitArrayValExpr(miniJavaExprParser.ArrayValExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constIdenExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterConstIdenExpr(miniJavaExprParser.ConstIdenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constIdenExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitConstIdenExpr(miniJavaExprParser.ConstIdenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code operationExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterOperationExpr(miniJavaExprParser.OperationExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code operationExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitOperationExpr(miniJavaExprParser.OperationExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code oppExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterOppExpr(miniJavaExprParser.OppExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code oppExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitOppExpr(miniJavaExprParser.OppExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code prioExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPrioExpr(miniJavaExprParser.PrioExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code prioExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPrioExpr(miniJavaExprParser.PrioExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code classPropExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterClassPropExpr(miniJavaExprParser.ClassPropExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code classPropExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitClassPropExpr(miniJavaExprParser.ClassPropExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constBooleanExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterConstBooleanExpr(miniJavaExprParser.ConstBooleanExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constBooleanExpr}
	 * labeled alternative in {@link miniJavaExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitConstBooleanExpr(miniJavaExprParser.ConstBooleanExprContext ctx);
}